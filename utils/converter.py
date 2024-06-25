class Converter:
    @staticmethod
    def time_to_seconds(hours=0, minutes=0, seconds=0):
        """将时分秒转换为秒"""
        return hours * 3600 + minutes * 60 + seconds

    @staticmethod
    def seconds_to_time(total_seconds):
        """将秒转换为时分秒格式"""
        hours = total_seconds // 3600
        remainder = total_seconds % 3600
        minutes = remainder // 60
        seconds = remainder % 60
        return hours, minutes, seconds

    @staticmethod
    def meters_to_kilometers(meters):
        """将米转换为千米"""
        return meters / 1000

    @staticmethod
    def kilometers_to_400m_units(kilometers):
        """将千米转换为四百米为单位"""
        return kilometers * 1000 / 400
