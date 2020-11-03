import boto3

client = boto3.client('translate', region_name="us-west-2")
phrase = "my name is Fahad"
result = client.translate_text(Text=phrase, SourceLanguageCode='auto', 
    TargetLanguageCode='ar')
text = result['TranslatedText'] 
print(text)