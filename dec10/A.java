import javafx.util.Pair;

import java.io.*;
import java.util.ArrayList;

public class A {
    public static void main(String[] args) throws Exception {

        //Reading file
        String wd = System.getProperty("user.dir");
        System.out.println(wd);
        File file = new File(wd + "\\input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        ArrayList<Pair<Integer,Integer>> coordinates = new ArrayList<Pair<Integer,Integer>>();
        String line;
        int i = 0;
        while ((line = br.readLine()) != null) {
            for (int j = line.indexOf('#'); j >= 0; j = line.indexOf('#', j + 1)) {
                coordinates.add(new Pair(i,j));
            }
            i++;
        }
        //Do thing

        Pair<Integer,Integer> xPair;
        Pair<Integer,Integer> yPair;
        int x = 0;
        int y = 0;
        int tempX = 0;
        int tempY = 0;

        int index = -1;
        int max = -1;

        //For each asteroid
        for (i = 0; i < coordinates.size(); i++){
            //Comparing to all other asteroid
            ArrayList<Pair<Integer,Integer>> asteroids = new ArrayList<Pair<Integer,Integer>>();
            xPair = coordinates.get(i);
            for (int j= 0; j < coordinates.size(); j++) {
                if (i != j) {
                    boolean newAsteroid = true;
                    yPair = coordinates.get(j);

                    x = xPair.getKey()-yPair.getKey();
                    y = xPair.getValue()-yPair.getValue();

                    for(Pair<Integer,Integer> a: asteroids){
                        tempX = a.getKey();
                        tempY = a.getValue();
                        if(x == 0) {
                            if (tempX == 0 && (((tempY > 0)&&(y > 0))||((tempY < 0)&&(y < 0)))) {newAsteroid = false; break;}
                        }
                        else if (y == 0) {
                            if (tempY == 0 && (((tempX > 0)&&(x > 0))||((tempX < 0)&&(x < 0)))) {newAsteroid = false; break;}
                        }
                        else {
                            if (((tempX % x == 0)&&(tempY % y == 0)) && (((tempY > 0)&&(y > 0))||((tempY < 0)&&(y < 0)))) {newAsteroid = false; break;}
                        }
                    }
                    if (newAsteroid) asteroids.add(new Pair(x,y));
                }
            }
            if(asteroids.size() > max) {
                index = i;
                max = asteroids.size();
            }

        }
        System.out.println("Asteroid at: " + coordinates.get(index));
        System.out.println("Result: " + max);
    }
}
