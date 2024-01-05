import java.io.IOException;
import java.util.*;
class 전화번호목록 {
    public static  boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        for (int i = 0; i < phone_book.length - 1; i++) {
              if (phone_book[i+1].startsWith(phone_book[i])) {
                  answer = false;
                  break;
              }
        }
        return answer;
    }

    // public static void main(String[] args) throws IOException {
    //     System.out.println(solution(new String[]{"123","456","789"}));
    // }
}