from    transformers            import  WhisperProcessor, WhisperForConditionalGeneration

def openai_summarizer(index = 3):
    """
    https://huggingface.co/openai/whisper-tiny
    """
    modelss =   [
                "openai/whisper-tiny",      #39m params useless
                "openai/whisper-base",      #74m params
                "openai/whisper-small",     #244m params very well
                "openai/whisper-medium",    #769m params
                "openai/whisper-large",     #1550m params
                "openai/whisper-large-v2",  #1550m params
                ]
    
    # load model and processor
    processor   = WhisperProcessor.from_pretrained(modelss[index])
    model       = WhisperForConditionalGeneration.from_pretrained(modelss[index]).to('cuda')
    model.config.forced_decoder_ids = None

    return processor,model
