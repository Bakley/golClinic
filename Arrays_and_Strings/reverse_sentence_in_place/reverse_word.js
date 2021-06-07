function reverseA(arr, start, end) {
    while (start < end) {
      let temp = arr[start]; 
      arr[start] = arr[end];
      arr[end] = temp;
      start++;
      end--;
    }
}

function reverseSentence(sent) {
    reverseA(sent, 0, sent.length - 1);
    let start = 0
    let end = 0
    while (start < sent.length) {
        // seeking the end of word
        while (end < sent.length && sent[end] != ' ') {
            end++;
        }
        reverseA(sent, start, end);
        start = end + 1;
    }
}

let sentence = "this is good".split('');
reverseSentence(sentence);
console.log(sentence)
