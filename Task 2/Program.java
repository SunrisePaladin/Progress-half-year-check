import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import Components.ConsoleView;

public class Program {
    static ConsoleView cv = null;

    public static void longestWord(ArrayList<String> words) {
        int length = 0;
        String curword = "";
        for (String word : words) {
            if (word.length() > length) {
                length = word.length();
                curword = word;
            }
        }
        System.out.printf("\nСамое длинное слово - %s, его длина - %d\n", curword, length);
    }

    public static void main(String[] args) {
        // System.out.println("Starting");
        cv = new ConsoleView();
        ArrayList<String> items = cv.getAll();

        int count = 0;

        HashMap<String, Integer> counts = new HashMap<String, Integer>();
        for (int i = 0; i < items.size(); i++) {
            // почему-то два пробела в тексте дают пустое слово
            if (items.get(i) != "") {
                count++;
                if (counts.containsKey(items.get(i))) {
                    counts.put(items.get(i), counts.get(items.get(i)) + 1);
                } else
                    counts.put(items.get(i), 1);
            }
        }
        System.out.println("1. Число слов - " + count);

        longestWord(items);
        analyze_rate(counts, count);

        // counts.entrySet().forEach(System.out::println);
    }

    private static void analyze_rate(HashMap<String, Integer> counts, int count) {
        for (Map.Entry<String, Integer> entry : counts.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            Double rate = (double)value/count*100;
            System.out.println(key + " встречается " + value + " раз, это " + Math.round(rate*100.0)/100.0 + "% текста");
        }
    }

}