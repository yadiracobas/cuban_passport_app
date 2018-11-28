passport_services_choice = (
	('first_time_passport','Pasaporte por primera vez'),
	('extend_passport', 'Prorroga de pasaporte'),
	('renew_passport', 'Renovacion de pasaporte')
	)

# class Passport(models.Model):
# 	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
# 	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
# 	passport_number = models.CharField(max_length=10)
# 	date_created = models.DateTimeField(default=timezone.now)
# 	service_type = models.CharField(choices=passport_services_choice, max_length=20)
