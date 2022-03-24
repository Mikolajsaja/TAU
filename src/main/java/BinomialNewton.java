public class BinomialNewton {
    public static long Newton( int n, int k )
    {
        long  Wynik = 1;
        int i;

        for(i = 1; i <= k; i++)
        {
            Wynik = Wynik * ( n - i + 1 ) / i;
        }

        return Wynik;
    }
}
