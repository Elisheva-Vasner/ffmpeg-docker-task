package password_checker;

import java.util.HashMap;

public class My_password_checker {

    public static void main(String[] args) {
        System.out.println(isStrongPassword("980#A6a1"));
    }

    public static boolean isStrongPassword(String password) {
        return isPasswordLengthValid(password) &&
               containsLowerCase(password) &&
               containsUpperCase(password) &&
               containsDigit(password) &&
               containsSpecialCharacter(password) &&
               doesNotContainCharMoreThanTwice(password) &&
               containsNoTripleConsecutiveChars(password);
    }

    public static boolean isPasswordLengthValid(String password) {
        return password.length() >= 8;
    }

    public static boolean containsLowerCase(String password) {
        return password.matches(".*[a-z].*");
    }

    public static boolean containsUpperCase(String password) {
        return password.matches(".*[A-Z].*");
    }

    public static boolean containsDigit(String password) {
        return password.matches(".*\\d.*");
    }

    public static boolean containsSpecialCharacter(String password) {
        return password.matches(".*[!@#$%^&*()_+\\-=\\[\\]{};':\"\\\\|,.<>/?].*");
    }

    public static boolean doesNotContainCharMoreThanTwice(String password) {
        HashMap<Character, Integer> counts = new HashMap<>();
        for (char c : password.toCharArray()) {
            counts.put(c, counts.getOrDefault(c, 0) + 1);
            if (counts.get(c) > 2) {
                return false;
            }
        }
        return true;
    }

    public static boolean containsNoTripleConsecutiveChars(String password) {
        for (int i = 0; i < password.length() - 2; i++) {
            char c1 = password.charAt(i);
            char c2 = password.charAt(i + 1);
            char c3 = password.charAt(i + 2);
            if (c2 == c1 + 1 && c3 == c2 + 1) {
                return false;
            }
        }
        return true;
    }
}
