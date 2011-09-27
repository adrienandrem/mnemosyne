#
# cards_added.py <Peter.Bienstman@UGent.be>
#

from mnemosyne.libmnemosyne.translator import D_, _
from mnemosyne.libmnemosyne.statistics_page import PlotStatisticsPage


class CardsAdded(PlotStatisticsPage):

    name = D_("Cards added")

    LAST_WEEK = 1
    LAST_MONTH = 2
    LAST_3_MONTHS = 3
    LAST_6_MONTHS = 4
    LAST_YEAR = 5

    variants = [(LAST_WEEK, D_("Last week")),
                (LAST_MONTH, D_("Last month")),
                (LAST_3_MONTHS, D_("Last 3 months")),
                (LAST_6_MONTHS, D_("Last 6 months")),                
                (LAST_YEAR, D_("Last year"))]

    def retranslate(self):
        self.name = _(self.name)
        for idx, variant in enumerate(self.variants):
            self.variants[idx] = (self.variants[idx][0],
                                  _(self.variants[idx][1]))

    def prepare_statistics(self, variant):
        if variant == self.LAST_WEEK:            
            self.x = range(-7, 1, 1)
        elif variant == self.LAST_MONTH:
            self.x = range(-31, 1, 1)
        elif variant == self.LAST_3_MONTHS:
            self.x = range(-91, 1, 1)
        elif variant == self.LAST_6_MONTHS:
            self.x = range(-182, 1, 1)
        elif variant == self.LAST_YEAR:
            self.x = range(-365, 1, 1)
        else:
            raise AttributeError, "Invalid variant"
        self.y = [self.database().card_count_added_n_days_ago(n=-day) \
                  for day in self.x]
        
            
