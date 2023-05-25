#Placecountwithkey
function(doc) {
  if (doc.doc && doc.doc.includes && doc.doc.includes.places && doc.doc.data && doc.doc.data.text) {
    var places = doc.doc.includes.places;
    var text = doc.doc.data.text.toLowerCase();
    var keyword = '';
    var count = 0;

    // Define the keywords to search for
    var keywords = ['alcohol', 'alcoholics', 'alcoholism', 'beer', 'booze', 'champagne', 'cocktail', 'drinking', 'drunk', 'gin', 'hangover', 'intoxicated', 'liquor', 'rum', 'spirits', 'tequila', 'vodka', 'whiskey', 'wine', 'brewery'];

    // Count the occurrences of keywords in the text
    for (var i = 0; i < keywords.length; i++) {
      if (text.includes(' ' + keywords[i] + ' ')) { // This ensures the keyword is not part of another word
        keyword = keywords[i];
        count++;
        if(count > 1) // If more than one keyword is found, reset keyword and count and break the loop
        {
          keyword = '';
          count = 0;
          break;
        }
      }
    }

    // Emit the full_name as the key and the keyword with the count as the value (only if count is 1)
    if (count === 1) {
      for (var j = 0; j < places.length; j++) {
        var full_name = places[j].full_name;
        emit(full_name, {keyword: keyword, count:count});
      }
    }
  }
}

#Sentiment
function(doc) {
    var text = doc.doc.data.text.toLowerCase(); // the text to be searched
    var keywords = ['alcohol', 'alcoholics', 'alcoholism', 'beer', 'booze', 'champagne', 'cocktail', 'drinking', 'drunk', 'gin', 'hangover', 'intoxicated', 'liquor', 'rum', 'spirits', 'tequila', 'vodka', 'whiskey', 'wine', 'brewery']; // keywords to search for
    for (var i in keywords) {
        var keyword = keywords[i];
        var regex = new RegExp("\\b" + keyword + "\\b", "i");
        if (regex.test(text)) {
            emit(doc.doc.data.author_id, {keyword: keyword, text: text}); // emit author_id and text
        }
    }
}



#placeCount
function(doc) {
  if (doc.doc && doc.doc.includes && doc.doc.includes.places) {
    var places = doc.doc.includes.places;
    var placeCounts = {};

    // Count the occurrences of each place in the places array
    for (var i = 0; i < places.length; i++) {
      var full_name = places[i].full_name;

      if (!placeCounts.hasOwnProperty(full_name)) {
        placeCounts[full_name] = 1;
      } else {
        placeCounts[full_name]++;
      }
    }

    // Emit the full_name as the key and the count as the value
    for (var place in placeCounts) {
      if (placeCounts.hasOwnProperty(place)) {
        emit(place, placeCounts[place]);
      }
    }
  }
}

#Mastodon_Sentiment
function(doc) {
    if (doc.content && doc.account && doc.account.acct) {  // Ensure content and acct exist
        var text = doc.content.toLowerCase(); // the text to be searched
        var keywords = ['alcohol', 'alcoholics', 'alcoholism', 'beer', 'booze', 'champagne', 'cocktail', 'drinking', 'drunk', 'gin', 'hangover', 'intoxicated', 'liquor', 'rum', 'spirits', 'tequila', 'vodka', 'whiskey', 'wine', 'brewery']; // keywords to search for
        for (var i in keywords) {
            var keyword = keywords[i];
            var regex = new RegExp("\\b" + keyword + "\\b", "i");
            if (regex.test(text)) {
                emit(doc.account.acct, {keyword: keyword, text: text}); // emit author_id and text
            }
        }
    }
}
