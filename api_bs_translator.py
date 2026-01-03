#!/usr/bin/env python3
# API Bullshit-to-English Translator
# Because "400: Bad Request" tells you exactly nothing

import re
import sys

def translate_error(error_msg):
    """Turns API nonsense into human words. Warning: May contain actual help."""
    
    # Our "translation" dictionary - because regex is basically magic
    patterns = {
        r'400.*[Bb]ad.*[Rr]equest': "You sent garbage. Check your JSON formatting.",
        r'401.*[Uu]nauthorized': "You forgot the magic password (token/API key).",
        r'403.*[Ff]orbidden': "You have the password but aren't invited to this party.",
        r'404.*[Nn]ot.*[Ff]ound': "You're asking for something that doesn't exist. Like unicorns.",
        r'429.*[Rr]ate.*[Ll]imit': "Slow down, turbo! You're hitting the API too fast.",
        r'500.*[Ii]nternal.*[Ss]erver': "Their code broke. It's not you, it's them. Probably.",
        r'502.*[Bb]ad.*[Gg]ateway': "The server is playing telephone and messed up the message.",
        r'503.*[Ss]ervice.*[Uu]navailable': "The server is taking a coffee break. Try again later.",
        r'[Tt]imeout': "The server got bored waiting and left. Your request took too long.",
        r'[Cc]onnection.*[Rr]efused': "The server door is locked. Check your URL/port.",
        r'[Ii]nvalid.*[Tt]oken': "Your 'magic key' expired or was never magic to begin with.",
        r'[Mm]issing.*[Pp]arameter': "You forgot to fill in a required field. Oops.",
        r'[Vv]alidation.*[Ee]rror': "You put text where numbers should be. Or vice versa."
    }
    
    # Find the first matching bullshit pattern
    for pattern, translation in patterns.items():
        if re.search(pattern, error_msg, re.IGNORECASE):
            return f"\n🤖 API says: '{error_msg}'\n💡 Translation: {translation}"
    
    # If all else fails, give generic advice (it's usually DNS anyway)
    return f"\n🤖 API says: '{error_msg}'\n💡 Translation: Something broke. Try: 1) Check docs 2) Validate data 3) Sacrifice a goat to the tech gods"

def translate_doc_sentence(sentence):
    """Translates documentation from corporate-speak to English."""
    translations = {
        'leverage': 'use',
        'synergy': 'work together',
        'paradigm': 'way of doing things',
        'robust': 'doesn't break easily',
        'scalable': 'handles more users',
        'seamless': 'hopefully works smoothly',
        'cutting-edge': 'new and possibly buggy',
        'enterprise-grade': 'expensive',
        'utilize': 'use',
        'optimize': 'make faster/better'
    }
    
    result = sentence
    for bs_word, normal_word in translations.items():
        result = re.sub(rf'\b{bs_word}\b', normal_word, result, flags=re.IGNORECASE)
    
    return f"\n📄 Docs say: {sentence}\n💬 Actually means: {result}"

def main():
    """Main function because every script needs one, apparently."""
    print("\n=== API Bullshit-to-English Translator ===\n")
    
    if len(sys.argv) > 1:
        # Command line mode
        user_input = ' '.join(sys.argv[1:])
        print(translate_error(user_input))
    else:
        # Interactive mode
        print("Enter API error or docs sentence (or 'quit'):")
        while True:
            user_input = input("\n> ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            if any(word in user_input.lower() for word in ['error', 'failed', 'invalid', 'unable']):
                print(translate_error(user_input))
            else:
                print(translate_doc_sentence(user_input))
    
    print("\n✅ Translation complete. Go fix your code now!")

if __name__ == "__main__":
    main()
