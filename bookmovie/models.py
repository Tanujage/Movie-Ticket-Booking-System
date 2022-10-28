from django.db import models
class customer(models.Model):
    fname = models.CharField(max_length=25, null=True, default='')
    sname = models.CharField(max_length=25, null=True, default='')
    mobno = models.BigIntegerField(null=True, default='')
    photo = models.ImageField(upload_to='Images/faces', height_field=None, width_field=None, max_length=None, null=True,
                              default='', blank=True)
    def __str__(self):
        return self.fname + ' ' + self.sname

class movie(models.Model):
    movie_img = models.ImageField(upload_to='Images/', null=True, blank=True)
    movie_name = models.CharField(max_length=50, null=True, default='')
    ticket_cost = models.IntegerField()
    movie_info = models.CharField(max_length=200, null=True, default='')
    lang = models.CharField(max_length=200, null=True, default='')
    booked_seat = models.ManyToManyField('Seat',null=True,blank=True)
    def __str__(self) :
        return f"{self.movie_name} (rs{self.ticket_cost})"

class Seat(models.Model):
    seat_no=models.IntegerField()
    occupant_first_name=models.CharField(max_length=255)
    occupant_last_name = models.CharField(max_length=255)
    occupant_email = models.CharField(max_length=255)
    purchase_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.occupant_first_name}-{self.occupant_last_name} seate_no{self.seat_no}"


