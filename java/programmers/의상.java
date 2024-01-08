import java.io.IOException;
import java.util.*;
class 의상 {
    public static int solution(String[][] clothes) {
        Map<String, Integer> clothingCountMap = new HashMap<>();
        for (String[] cloth : clothes) {
            String type = cloth[1];
            clothingCountMap.merge(type, 1, Integer::sum);
        }

        int answer = 1;
        for (Map.Entry<String, Integer> entry : clothingCountMap.entrySet()) {
            int count = entry.getValue();
            answer *= (count + 1);
        }
        answer -= 1;
        return answer;
    }
    public static void main(String[] args) throws IOException {
        System.out.println(solution(new String[][]{{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}, {"crow_mask", "face"}}));
    }
}

