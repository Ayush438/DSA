# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

#  prices=  [7  2  4  5  1  3  6  4]                                              #update buy price only if new price is lower
                                                                                  #try to sell if new price > buy_price
                                                                                  #curr profit=Today's price-buy_price
                                                                                  #update max profit

    def maxProfit(self, prices):

        buy_price=prices[0]
        max_profit=0

        for i in range(1,len(prices)):
            cur_profit=prices[i]-buy_price
            if prices[i]<buy_price:
                buy_price=prices[i]
            if max_profit < cur_profit:
                max_profit=cur_profit
        return max_profit
        
