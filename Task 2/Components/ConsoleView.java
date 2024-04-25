package Components;

import Interfaces.View;
import java.io.BufferedReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class ConsoleView implements View{

    public static ArrayList<String> readFile(BufferedReader reader) throws IOException
    {
        String str = reader.readLine().toLowerCase();
        String[] words = str.split(" ");
        ArrayList<String> strings = new ArrayList<String>(Arrays.asList(words));
        return strings;
    }

    public String get() {
        // return in.next();
        return "amogus";
    };

    public ArrayList<String> getAll(){

        ArrayList<String> content = null;
        Charset charset = StandardCharsets.UTF_8;
        String filename = "Task 2/Components/data.txt";
        Path path = Paths.get(filename);
        try (BufferedReader reader = Files.newBufferedReader(path, charset)) {
            content = readFile(reader);
            // reader.close();
        } 
        catch (IOException e) {
            e.printStackTrace();
        }
        
        return content;
    }

    @Override
    public void set(String value) {
        System.out.println(value);
    }
}

