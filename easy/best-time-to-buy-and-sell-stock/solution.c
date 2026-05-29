int maxProfit(int* prices, int pricesSize) 
{
    if(pricesSize < 2) return 0;

    int min = prices[0];
    int max = 0;

    for(int i = 0; i < pricesSize; i++)
    {
        if(prices[i] - min > max) max = prices[i] - min;

        if(prices[i] < min) min = prices[i];
    }

    return max;
}