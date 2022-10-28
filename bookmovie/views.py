import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import  render, redirect, HttpResponse
import razorpay
import face_recognition as fr
import numpy as np
import cv2
import os
import logging
from .models import customer,movie
from .form import customform
def login(request):
    return render(request, 'login.html')
def payment(request):
    return render(request, 'payment.html')
def signup(request):
    return render(request, 'signup.html')
def book(request):
    return render(request, 'booking_confermed.html')
def home(request):
    return render(request, 'home.html')
def seat(request):
    return render(request, 'seat.html')

def userlist(request):
    users = movie.objects.all()
    return render(request, 'seat.html', {'users': users, })

def movielist(request):
    movies = movie.objects.all()
    return render(request, 'home.html', {'movies': movies, })
@csrf_exempt
def OccupiedSeat(request):
    data=json.loads(request.body)
    Movie= movie.objects.get(movie_name=data["movie_name"])
    occupied=Movie.booked_seat.all()
    occupied_seat = list(map(lambda seat: seat.seat_no-1,occupied))

    return JsonResponse({
        "occupied_seat":occupied_seat,
        "movie":str(Movie)
    })

def insertrecord(request):
    if request.method == 'POST':
        Customer_form = customform(request.POST, request.FILES)
        if Customer_form.is_valid():
            cust = Customer_form.save(commit=False)
            Customer_form.save(commit=True)


            return redirect('login')

    else:
        Customer_form = customform()

    context = {'Customer_form': Customer_form, }

    return render(request, 'signup.html', context)


# folder path
dir_path = r'C:\Users\HP\PycharmProjects\miniproject_sem5\bookmovie\media\Images\faces'

# Iterate directory
count = 0
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        count = count + 1

best_match_index = ''
matches = ''

def cam(request):
    global best_match_index, frame
    global matches
    logging.basicConfig(filename="camerafunction.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    global video
    logger.info("camera starting")
    video = cv2.VideoCapture(0)
    logger.info("camera started")
    try :
        logger.info("Starting first for loop")
        for file in os.listdir(dir_path) :
            filename = dir_path + "/" + file
            logger.info("Load Image File")
            image = fr.load_image_file(filename)  # imagefile
            logger.info("Loading Image File Completed and Starting Encoding")
            image_encodings = fr.face_encodings(image)[0]  # writes image data to a string
            logger.info("Encoding done")
            known_face_encodings = [image_encodings]  # array of known face encoding
            known_face_name = [file]  # array of names
            logger.info("Starting Video Read")

            ret, frame = video.read()
            logger.info("End Video Read")
            rgb_frame = frame[:, :, : :-1]  # convet color of the frame to rgb frame
            face_locations = fr.face_locations(rgb_frame)  # to find the face locations
            face_encodings = fr.face_encodings(rgb_frame, face_locations)

            logger.info("Starting second for loop")
            for (top, right, bottom, left), face_encodings in zip(face_locations,
                                                                  face_encodings) :  # zip to combain two or more iterables
                logger.info("Starting compare_faces")
                matches = fr.compare_faces(known_face_encodings, face_encodings, tolerance=0.45)
                logger.info("End compare_faces")
                name = "unkown"
                logger.info("Calculating face distance")
                face_distances = fr.face_distance(known_face_encodings,
                                                  image_encodings)  # compairs the distance between 2 points of the face
                logger.info("Calculation done")
                best_match_index = np.argmin(face_distances)  # best match is the image with similar face distances
                logger.info("Found best match")

            if matches[best_match_index]:
                name = known_face_encodings[best_match_index]
                video.release()
                cv2.destroyAllWindows()
                logger.info("Returning Success View")
                return redirect("home")
            else:
                logger.info("Returning fail View")
                continue

            cv2.imshow('webcame_facerecog', frame)
            if cv2.waitKey(1) and 0xff == ord('q') :
                break
            break
        logger.info("Returning failed view")
        return render(request, 'user_not_found.html')

    except Exception:
        logger.info("Error occurred")
        return render(request, 'user_not_found.html')