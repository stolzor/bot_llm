from pydantic_settings import BaseSettings
import os


class AdvancedBaseSettings(BaseSettings):
    """
    Parent class for inheritance
    """

    @staticmethod
    def get_dir() -> str:
        """Get dir parent class

        Returns:
            str: row dir
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path
