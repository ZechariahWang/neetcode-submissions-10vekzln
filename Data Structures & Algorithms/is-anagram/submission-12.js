class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    objectEquals(a,b){
        const keysA=Object.keys(a);
        const keysB=Object.keys(b);

        if (keysA.length !== keysB.length) {
            return false;
        }

        for (let key of keysA) {
            if (a[key] !== b[key]){
                return false;
            }
        }
        return true;
    }

    isAnagram(s, t) {
        let countS={}
        let countT={}

        for (let c of s){
            countS[c]=(countS[c] || 0)+1;
        }
        for (let c of t){
            countT[c]=(countT[c] || 0) +1;
        }

        return this.objectEquals(countS,countT);
    }
}
