
def django_lang_code_to_rpx_lang_preference(lang_code, default = 'en'):
    '''
    Given django's internal LANGUAGE_CODE (full list can be found http://www.
    i18nguy.com/unicode/language-identifiers.html), returns the equivalent language
    preference code that is used by RPX to specify localization of the sign in 
    interface (see https://rpxnow.com/docs#sign-in_localization).
    
    For LANGUAGE_CODE with dashes in them (ex. 'de-at'), this function will try to
    match 'de-at' first, then 'en-AT', and finally 'de'. If no mapping is
    found, the returned language preference will default to 'en'.
    
    Essentially, RPX is stupid and can't handle the language code standard. They
    use their own language code system.

    (Contributed by philotas, http://github.com/philotas)
    '''
    #From https://rpxnow.com/docs#sign-in_localization (as of May 21, 2010)
    rpx_lang_codes = ('cs', 'da', 'de', 'el', 'en', 'es', 'fr', 'he', 'hr',
                       'it', 'ja', 'lt', 'nl', 'nl-BE', 'nl-NL', 'pl', 'pt',
                       'pt-BR', 'pt-PT', 'ro', 'ru', 'sl', 'sv', 'sv-SE', 'th',
                       'zh')
    
    if lang_code in rpx_lang_codes:
        return lang_code

    #Handle language code with dashes in them. We already checked for exact case
    #(ex. 'de-at'). Now we want to check for where the second part is upper case
    #(ex. 'de-AT'). If that doesn't match, then we just check for the first part 
    #without the dash (ex. 'de').
    if '-' in lang_code:
        lang, specific = lang_code.split('-', 1)
        lang_code = '%s-%s' % (lang, specific.upper())
        #Check for uppercase version:
        if lang_code in rpx_lang_codes:
            return lang_code
        #Otherwise, check the first part:
        if lang in rpx_lang_codes:
            return lang

    #We have no matches, so return default ('en' if not set) 
    return default
