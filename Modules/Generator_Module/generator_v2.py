def gpt2_generator():
    import torch
    from transformers import GPT2LMHeadModel, GPT2Tokenizer
    from generate_text_v1 import clean_to_pass
    # initialize tokenizer and model from pretrained GPT2 model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    model = GPT2LMHeadModel.from_pretrained('gpt2')


    list_of_sequences = [
    'Out of office during the 1930s, Churchill took the lead in calling for British rearmament to counter the growing threat of militarism in Nazi Germany. At the outbreak of the Second World War he was re-appointed First Lord of the Admiralty. In May 1940, he became Prime Minister, replacing Neville Chamberlain. Churchill oversaw British involvement in the Allied war effort against the Axis powers, resulting in victory in 1945. After the Conservatives defeat in the 1945 general election, he became Leader of the Opposition',
    'Artificial intelligence was founded as an academic discipline in 1955, and in the years since has experienced several waves of optimism,followed by disappointment and the loss of funding (known as an "AI winter"), followed by new approaches, success and renewed funding. After AlphaGo successfully defeated a professional Go player in 2015, artificial intelligence once again attracted widespread global attention',
    'Technology has many effects. It has helped develop more advanced economies (including todays global economy) and has allowed the rise of a leisure class. Many technological processes produce unwanted by-products known as pollution and deplete natural resources to the detriment of Earths environment. Innovations have always influenced the values of a society and raised new questions in the ethics of technology. Examples include the rise of the notion of efficiency in terms of human productivity, and the challenges of bioethics',
    'Nature has furnished us with numerous significant assets like water, air, food, therapeutic plants, fire, fuels, woods, and trees, and so forth. Every one of these assets helps us for different purposes. As a whole, we realize that our endurance will turn out to be difficult or end without them. As they serve us, they likewise need our adoration and service.',
    'We should love every creation of God, regardless of whether a plant or a creature. We should treat them with affection, and attempt to secure them, however much as it is possible to do. Likewise, cherishing nature incorporates keeping the air and water clean, planting numerous trees, taking care of the variety of animals, treating harmed creatures or helpless humans, and so on. Our acts of love will include a touch of paradise the earth',
    'Everybody makes a few companions at various phases of life. A few companionships last more while some end in only a couple of months. The fundamental explanation for it is the presence of love. Indeed, even we ought to have a sentiment of affection for the needy and poor. They deserve our love the most. We should that is why show our love and affection to everybody irrespective of any differences among each other'
                    ]
    import random
    sequence = list_of_sequences[random.randint(0, 5)]
    
    inputs = tokenizer.encode(sequence, return_tensors='pt')

    # we pass a maximum output length of 200 tokens
    outputs = model.generate(inputs, max_length=400, do_sample=True)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    clean_text = clean_to_pass(text)

    return {
    'to_read':text,
    'to_check':clean_text
    }