import java.util.Scanner;

public class SimpleCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 提示用户输入第一个数字
        System.out.print("请输入第一个数字: ");
        double num1 = scanner.nextDouble();

        // 提示用户输入运算符
        System.out.print("请输入运算符 (+, -, *, /): ");
        char operator = scanner.next().charAt(0);

        // 提示用户输入第二个数字
        System.out.print("请输入第二个数字: ");
        double num2 = scanner.nextDouble();

        double result;

        // 根据运算符执行相应的运算
        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                // 检查除数是否为零
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    System.out.println("错误: 除数不能为零");
                    return;
                }
                break;
            default:
                System.out.println("错误: 无效的运算符");
                return;
        }

        // 输出结果
        System.out.println("结果是: " + result);
    }
}