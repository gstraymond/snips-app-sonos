

class NodeSearchQueryBuilder(object):

    AVAILABLE_MUSIC_SERVICES = ["spotify", "deezer"]

    PORT = 5005
    HOST = "localhost"
    PROTOCOL = "http://"

    def __init__(self, device, music_service):
        self.device = device
        self.music_service = music_service
        self.result_type = None
        self.field_filters = []

    def set_music_service(self, music_service):
        if self.is_available_music_service(music_service):
            self.music_service = music_service
        # TODO throw error

    def add_result_type(self, result_type):
        self.result_type = result_type
        return self

    def add_track_result_type(self):
        return self.add_result_type("song")

    def add_album_result_type(self):
        return self.add_result_type("album")

    def add_playlist_result_type(self):
        return self.add_result_type("playlist")

    def add_track_filter(self, track_name):
        self.field_filters.append(track_name)
        return self

    def add_artist_filter(self, artist_name):
        self.field_filters.append(artist_name)
        return self

    def add_album_filter(self, album_name):
        self.field_filters.append(album_name)
        return self

    def add_playlist_filter(self, playlist_name):
        self.field_filters.append(playlist_name)
        return self

    def _generate_base_endpoint(self):
        return "{}{}:{}".format(self.PROTOCOL, self.HOST, self.PORT)

    def _generate_query_terms(self):
        return ''.join(["{} ".format(field_filter for field_filter in self.field_filters)])\
            .strip()

    def generate_search_query(self):
        room_name = self.device.name
        base_endpoint = self._generate_base_endpoint()
        fields_query = self._generate_query_terms()
        if self.result_type and fields_query:
            return "{}/{}/{}/{}/{}".format(base_endpoint, room_name, self.music_service,
                                           self.result_type, fields_query)
        else:
            print("Create error case")  # TODO

    def is_available_music_service(self, music_service):
        return music_service in self.AVAILABLE_MUSIC_SERVICES
