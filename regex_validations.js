const regexPatterns = {
	  email: /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b/g,
	 url: /https?:\/\/(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/\S*)?/g,
	  
	  phone: /(\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}/g,
	  
	  creditCard: /\b(?:\d{4}[- ]?){3}\d{4}\b/g
};
function extractMatches(text, pattern) {
	  return text.match(pattern) || [];
}
module.exports = {
	  regexPatterns,
	  extractMatches
};
