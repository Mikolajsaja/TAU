import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class BinomialNewtonTest {

    @Test
    public void resultOfBinomialNewtonWhenTheyAreDifferent() {
        long Wynik = BinomialNewton.Newton(3, 2);
        Assertions.assertEquals(3, Wynik);
    }

    @Test
    public void resultOfBinomialNewtonWhenTheyAreTheSame() {
        long Wynik = BinomialNewton.Newton(5, 5);
        Assertions.assertEquals(1, Wynik);
    }

    @Test
    public void resultOfBinomialNewtonWhenThereIsValueZero() {
        long Wynik = BinomialNewton.Newton(5, 0);
        Assertions.assertEquals(1, Wynik);
    }

    @Test
    public void resultOfBinomialNewtonWhenBothVariablesAreZero() {
        long Wynik = BinomialNewton.Newton(0, 0);
        Assertions.assertEquals(1, Wynik);
    }

    @Test
    public void resultOfBinomialNewtonWhenVeryLargeNumber() {
        long Wynik = BinomialNewton.Newton(15000, 10);
        Assertions.assertEquals(1, Wynik);
    }

    @Test
    public void resultOfBinomialNewtonWhenNIsLowerThanK() {
        long Wynik = BinomialNewton.Newton( 1 ,10);
        Assertions.assertEquals(0, Wynik);
    }

    @Test
    public void resultOfBinomialNewtonWhenWhenInsideIsMathematicalOperationOfMultiplication() {
            long Wynik = BinomialNewton.Newton(5*2, 2);
            Assertions.assertEquals(45, Wynik);
    }

    @Test
    public void resultOfBinomialNewtonWhenWhenInsideIsMathematicalOperationOfDividing() {
        long Wynik = BinomialNewton.Newton(9/2, 2);
        Assertions.assertEquals(45, Wynik);
    }

    @Test
    public void resultOfBinomialNewtonWhenWhenBothAreUsedInMathematicalOperation() {
        long Wynik = BinomialNewton.Newton(8+4, 9-3);
        Assertions.assertEquals(924, Wynik);
    }
}
