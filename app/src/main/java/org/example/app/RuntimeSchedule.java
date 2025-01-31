// This is the main structure of the programe. App.java is the surface, this file is the core.

package org.example.app;
import java.util.Scanner;


class KeyboardInput {  
    private static Scanner scanner = new Scanner(System.in); // 共享 Scanner 实例

    public static String takeInput() {  // 让方法变成静态，便于直接调用
        return scanner.nextLine();
    }

    public static void closeScanner() { // 关闭 Scanner 的方法，防止资源泄露
        scanner.close();
    }
}

class Start {
    private static void cover() {
        
        System.out.print("Ready to pass through? \n >");
        
        String userInput = KeyboardInput.takeInput(); // 直接调用静态方法获取输入

        //System.out.println("You entered: " + userInput);
        if (userInput.equals("")){

        }
    }
}



/**
 VERY IMPORTANT !!!
 **/
public class RuntimeSchedule {
    public static void main(String[] args){

        Boolean working = false;

        //while(!working){
        
        KeyboardInput.closeScanner(); // 关闭 Scanner
    }
}

