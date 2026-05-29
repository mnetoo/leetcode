class Solution 
{
    public int removeDuplicates(int[] nums) 
    {
        if (nums.length <= 2) return nums.length;

        // k é a posição onde o próximo elemento válido deve ser colocado
        // k = 2 pq os dois primeiro elementos sempre serão válidos
        int k = 2;

        for (int i = 2; i < nums.length; i++) 
        {
            // Se o elemento atual for diferente do elemento na posição k-2,
            // significa que não temos três (ou mais) repetições consecutivas.
            if (nums[i] != nums[k - 2]) 
            {
                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }
}