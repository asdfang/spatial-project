# scrapy crawl niche -o zip_grades.csv -t csv

import scrapy

class NicheSpider(scrapy.Spider):
    name = "niche"

    def start_requests(self):
        zip_codes = [60201]
        # chicago_zip_codes = [60290, 60601, 60602, 60603, 60604, 60605, 60606, 60607, 60608, 60610, 60611, 60614, 60615, 60618, 60619, 60622, 60623, 60624, 60628, 60609, 60612, 60613, 60616, 60617, 60620, 60621, 60625, 60626, 60629, 60630, 60632, 60636, 60637, 60631, 60633, 60634, 60638, 60641, 60642, 60643, 60646, 60647, 60652, 60653, 60656, 60660, 60661, 60664, 60639, 60640, 60644, 60645, 60649, 60651, 60654, 60655, 60657, 60659, 60666, 60668, 60673, 60677, 60669, 60670, 60674, 60675, 60678, 60680, 60681, 60682, 60686, 60687, 60688, 60689, 60694, 60695, 60697, 60699, 60684, 60685, 60690, 60691, 60693, 60696, 60701]
        # zip_codes = chicago_zip_codes

        niche_zip_url = 'https://www.niche.com/places-to-live/z/'
        urls = []
        for zip_code in zip_codes:
            urls.append(niche_zip_url + str(zip_code) + '/')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        grade_mapping = {
            'A+': 12,   'A': 11,    'A-': 10,
            'B+': 9,    'B': 8,     'B-': 7,
            'C+': 6,    'C': 5,     'C-': 4,
            'D+': 3,    'D': 2,     'D-': 1,
        }
        pdict = {}

        # Zip Code
        zip_code = response.request.url.split('/')[-2]
        pdict['Zip Code'] = zip_code

        # Overall Grade
        profile_buckets = response.css('div.profile__buckets')
        overall_grade = profile_buckets.css('div.overall-grade__niche-grade div::text').get()
        pdict['Overall Grade'] = grade_mapping[overall_grade]

        # Individual Grades
        individual_grades = profile_buckets.css('ol li.ordered__list__bucket__item')
        for g in individual_grades:
            grade_name = g.css('div.profile-grade__label::text').get()
            grade = g.css('div.niche__grade::text').get()

            pdict[grade_name] = grade_mapping[grade]

        yield pdict

        