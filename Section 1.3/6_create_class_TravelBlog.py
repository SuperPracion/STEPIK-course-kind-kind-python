class TravelBlog:
    total_blogs = 0

    def __init__(self, name, days):
        self.name = name
        self.days = days
        TravelBlog.total_blogs += 1

tb1 = TravelBlog('Франция', 6)
tb2 = TravelBlog('Италия', 5)
