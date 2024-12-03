# This represents our addition to the researchers source code.
#   It uses the same footprint so that the rest of the source code can be used to process this.
#   
#   **Add to DLModel.py just above the line:
#       "def buildBGRU(maxlen, vector_dim, layers, dropout, myoptimizer):"

from keras.layers import SimpleRNN

# The name here is one of two changes made to the source "buildBGRU"
def buildBRNN(maxlen, vector_dim, layers, dropout, myoptimizer): 
    print('Build model...')
    model = Sequential()
    
    model.add(Masking(mask_value=0.0, input_shape=(maxlen, vector_dim)))
    
    for i in range(1, layers):
        # This is the second change: GRU -> SimpleRNN; and removed the param: "recurrent_activation"
        model.add(Bidirectional(SimpleRNN(units=256, activation='tanh', return_sequences=True)))
        model.add(Dropout(dropout))
        
    model.add(Bidirectional(GRU(units=256, activation='tanh', recurrent_activation='hard_sigmoid')))
    model.add(Dropout(dropout))
    
    model.add(Dense(1, activation='sigmoid'))
    
    TP_count = TruePositives()
    TN_count = TrueNegatives() 
    FP_count = FalsePositives() 
    FN_count = FalseNegatives()
    
    model.compile(loss='binary_crossentropy', optimizer = myoptimizer, metrics=['accuracy'])
    model.summary()
 
    return model