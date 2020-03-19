import java.io.*;

public class A {
    public static void main(String[] args) throws Exception {
        int x = 25;
        int y = 6;

        //Reading file
        String wd = System.getProperty("user.dir");
        System.out.println(wd);
        File file = new File(wd + "\\input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        String st = br.readLine();

        //Do thing
        String[] list = st.split("(?<=\\G.{" + (x*y) + "})");
        int index = -1;
        int minZeros = 150;
        int temp = -1;
        for(int i= 0; i < list.length; i++){
            temp = (int) list[i].chars().filter(ch -> ch == '0').count();
            if(temp < minZeros) {
                minZeros = temp;
                index = i;
            }
        }

        System.out.println("Answer: " + list[index].chars().filter(ch -> ch == '1').count() * list[index].chars().filter(ch -> ch == '2').count());
    }
}
