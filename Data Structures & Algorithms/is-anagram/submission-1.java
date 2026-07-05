class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> chars = new HashMap<>();

            for (char c : s.toCharArray()) {
            if (chars.containsKey(c)) {
                chars.replace(c, chars.get(c) + 1);
            } else {
                chars.put(c, 1);
            }
        }

        for (char c : t.toCharArray()) {
            if (chars.containsKey(c)) {
                if (chars.get(c) > 1) {
                    chars.replace(c, chars.get(c) - 1);
                } else {
                    chars.remove(c);
                }

            } else {
                return false;
            }
        }

        return chars.isEmpty();
    }
}
