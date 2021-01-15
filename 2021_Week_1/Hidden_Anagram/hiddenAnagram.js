const hiddenAnagram = (text, phrase) => {
    const sorted = [...phrase.toLowerCase()].filter((char) => /[a-zA-Z]/.test(char)).sort().join('') ;
    const filteredText = [...text].filter((char) => /[a-zA-Z]/.test(char)).join('').toLowerCase() ;
    for( let i =  0; i + sorted.length <= filteredText.length ; ++i ) {
        const currentString = filteredText.slice(i, i + sorted.length ) ;
        const sortedCurrentString = [...currentString].sort().join('').toLowerCase() ;
        if (sortedCurrentString === sorted )
            return currentString ;
    }

    return "noutfond";
};