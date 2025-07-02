function solution(today, terms, privacies) {
    var answer = [];
    let [tYear, tMonth, tDay] = today.split(".").map(Number);
    for (let i = 0; i < privacies.length; i++){
        let [privacieseDate, privaciesType] = privacies[i].split(" ");
        let [pYear, pMonth, pDay] = privacieseDate.split(".").map(Number);
        for (let j = 0; j < terms.length; j++){
            let [termsType, termsMonth] = terms[j].split(" ");
            termsMonth = Number(termsMonth);
            if (termsType === privaciesType){
                pMonth += termsMonth;
                pYear += Math.floor((pMonth - 1) / 12);
                pMonth = ((pMonth - 1) % 12) + 1;
            }
        }
        pDay -= 1;
        if (pDay === 0) {
            pDay = 28;
            pMonth -= 1;
            if (pMonth === 0) {
                pMonth = 12;
                pYear -= 1;
            }
        }
        if (tYear > pYear){
            answer.push(i+1);
            continue;
        }
        if (tYear === pYear && tMonth > pMonth){
            answer.push(i+1);
            continue;
        }
        if (tYear === pYear && tMonth === pMonth && tDay > pDay){
            answer.push(i+1);
            continue;
        }
    }
    return answer;
}