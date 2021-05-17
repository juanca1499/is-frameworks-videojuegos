from django.core.validators import RegexValidator, FileExtensionValidator

foto_validator = FileExtensionValidator(
    allowed_extensions = ['png','jpeg','jpg'],
    message = 'Sólo se permiten imágenes PNG, JPG o JPEG.'
)