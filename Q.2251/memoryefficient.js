/**
 * @param {number[][]} flowers
 * @param {number[]} people
 * @return {number[]}
 */
var fullBloomFlowers = function(flowers, people) {
    let start = [];
    let end = [];
    let length = flowers.length;
    for(let i = 0; i < length;i++)
    {
        start[i]  = flowers[i][0];
        end[i] = flowers[i][1];
    }
    for(let i = 1; i < length; i++)
    {
        let j = i-1;
        let temp1 = start[i];
        let temp2 = end[i];
        let x = i-1;
        while(j>=0 && start[j] > temp1)
        {
            start[j+1] = start[j];
            j--;
        }
        start[j+1] = temp1;
        while(x>=0 && end[x] > temp2)
        {
            end[x+1] = end[x];
            x--;
        }
        end[x+1] = temp2;
    };

    for(let i = 0; i < people.length; i++)
    {
        let value;
        let time = people[i];
        let begin = 0;
        let last = length-1;
        let middle;
        while(begin <= last)
        {
            middle = Math.floor((begin+last)/2);
            if(start[middle] > time) last = middle-1;
            else begin = middle+1;
        };
        if(start[middle] > time) value = middle;
        else value = middle+1;
        begin = 0;
        last = length-1;
        while(begin <= last)
        {
            middle = Math.floor((begin+last)/2);
            if(end[middle] >= time) last = middle-1;
            else begin = middle+1;
        };
        if(end[middle] < time) value -= middle+1;
        else value -= middle;
        people[i] = value;
    }
    return people;
};
