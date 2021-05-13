class CompoundInterest:
    
    # RESULT = PRINCIPLE_AMOUNT(1+ RATE_OF_INTEREST/N_TIMES_COMPOUNDED_ANNUM) NO_Y_INVESTED * N_TIMES_COMPOUNDED_ANNUM
    
    def __init__(self, compound_frequency):
        self.comp_freq = compound_frequency
        pass

    def calculate(self, principle, rate, length):
        #return round((principle(1+rate/self.comp_freq)*length*self.comp_freq))
        return round((principle * pow((1+rate/self.comp_freq), (length*self.comp_freq))),2)

    # def calculate_with_cont(self, priciple, rate, length, contribution):
    #     total = priciple
    #     for n in range(1, (length*12)):
    #         total = (total*(1+rate))+contribution
    #     return total
            
