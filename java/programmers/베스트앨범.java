import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;
class 베스트앨범 {
    static class Music {
        int sumPlay;
        int firstIdx;
        int firstVal;
        int secondIdx;
        int secondVal;
        public Music() {
            this.sumPlay = 0;
            this.firstIdx = -1;
            this.firstVal = 0;
            this.secondIdx = -1;
            this.secondVal = 0;
        }

        public void addValue(int idx, int value){
            if(this.secondVal < value) {
                if (this.firstVal < value) {
                    this.secondVal = this.firstVal;
                    this.secondIdx= this.firstIdx;
                    this.firstVal = value;
                    this.firstIdx = idx;
                } else {
                    this.secondVal = value;
                    this.secondIdx= idx;
                }
            }
            this.sumPlay += value;
        }

        public int getSum() {
            return this.sumPlay;
        }
        public int getSecondIdx() {
            return this.secondIdx;
        }
        public int getFirstIdx() {
            return this.firstIdx;
        }
    }
    public static List<Integer> solution(String[] genres, int[] plays) {
        // List<Integer> answer = new ArrayList<>();
        Map<String, Music> genrePlayList = new HashMap<>();
        for (int i=0;i<genres.length;i++){
            Music music = genrePlayList.getOrDefault(genres[i], new Music());
            music.addValue(i, plays[i]);
            genrePlayList.put(genres[i], music);
        }
        List<Integer> answer = new ArrayList<>();
        List<Map.Entry<String, Music>> tempList = new ArrayList<>(genrePlayList.entrySet());
        tempList.stream()
        .sorted(Comparator.comparing(entry -> -1*entry.getValue().getSum()))
        .forEach(entry->{
            Music music = entry.getValue();
            answer.add(music.getFirstIdx());
            if(music.getSecondIdx()!= -1) answer.add(music.secondIdx);
        });
        // tempList sort by tempList sumplay
        return answer;
    }
    public static void main(String[] args ) throws IOException {
        System.out.println(solution(new String[]{"classic", "pop", "classic", "classic", "pop"}, new int[]{500, 600, 150, 800, 2500}));
    }
}

