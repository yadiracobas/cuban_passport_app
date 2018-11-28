from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. ''Unselect this instead of deleting accounts.'
        ),
    )

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.get_full_name()

    def __str__(self):
        return self.email

eyes_color_choices = (
	('light', 'Claros'),
	('Black', 'Negros'),
	('brown', 'Pardos'),	
	)

skin_color_choices = (
	('white', 'Blanco'),
	('black', 'Negra'),
	('yellow', 'Amarilla'),
	('mulatto', 'Mulata'),
	('albino', 'Albina')
	)

hair_color_choices = (
	('hoary', 'Canoso'),
	('black', 'Negro'),
	('blonde', 'Rubio'),
	('red', 'Rojo'),
	('brown', 'Castano'),
	('others', 'Otros')
	)


sex_choices = (
	('female', 'Femenino'),
	('male', 'Masculino')
	)

departure_choice = (
	('official_matter', 'Asunto oficial'),
	('pvt','PVT'),
	('pre_psi', 'PRE/PSI'),
	('psd', 'PSD'),
	('pve', 'PVE'),
	('ilegal', 'Ilegal')
	)

def no_future_date(value):
    today = date.today()
    if value > today:
        raise ValidationError('Revise sus datos, la fecha no debe ser futura')

# class Profile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     #general data
#     father_first_name = models.CharField(max_length=30, verbose_name='Nombre de su padre')
#     mother_first_name = models.CharField(max_length=30, verbose_name='Nombre de su madre')
#     height = models.CharField(max_length=10, verbose_name='Altura', 
#     	help_text='Aparece en su ID o licencia')
#     eyes_color = models.CharField(choices=eyes_color_choices, max_length=10, 
#     	default='brown', verbose_name='Color de sus ojos')
#     skin_color = models.CharField(choices=skin_color_choices, max_length=50, 
#     	default='white', verbose_name='Color de su piel')
#     hair_color = models.CharField(choices=hair_color_choices, max_length=50, 
#     	default='brown', verbose_name='Color de su pelo')    
#     date_of_birth = models.DateField(verbose_name='Fecha de nacimiento', 
#     	help_text='Use el formato MM/DD/AAAA',
#     	validators=[no_future_date])
#     country_of_birth = models.CharField(max_length=50, default='Cuba', 
#     	verbose_name='Pais de nacimiento')
#     province_of_birth = models.CharField(max_length=50, verbose_name='Provincia de nacimiento')
#     municipality_of_birth = models.CharField(max_length=50, verbose_name='Municipio de nacimiento')
    
#     departure_type = models.CharField(choices=departure_choice, max_length=30, 
#     	verbose_name='Forma de salida de Cuba', default='pve')
#     departure_date = models.DateField(verbose_name='Fecha de ultima salida de Cuba', 
#     	validators=[no_future_date])

#     #contact info
#     phone_number = models.CharField(max_length=50, verbose_name='Telefono')
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#     def __str__(self):
#     	return self.user.get_full_name()