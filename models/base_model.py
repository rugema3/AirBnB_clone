from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Define BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Define class constructor."""
        self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, self.datetime_format)
                if key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            self.datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
            self.add_to_storage()

    def __str__(self):
        """Define string representation of the object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Define save method."""
        self.updated_at = datetime.today()
        self.update_storage()

    def to_dict(self):
        """Define to_dict method."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__
        }

    def add_to_storage(self):
        """Add the object to the storage."""
        from models import storage
        storage.new(self)

    def update_storage(self):
        """Update the object in the storage."""
        from models import storage
        storage.save()
