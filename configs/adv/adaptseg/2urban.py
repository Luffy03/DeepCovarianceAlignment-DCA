from configs.ToURBAN import SOURCE_DATA_CONFIG,TARGET_DATA_CONFIG, EVAL_DATA_CONFIG, TARGET_SET


MODEL = 'ResNet'

IGNORE_LABEL = -1
MOMENTUM = 0.9
NUM_CLASSES = 7

SAVE_PRED_EVERY = 2000
SNAPSHOT_DIR = './log/adaptseg/2rural_lr5e-3'

#Hyper Paramters
WEIGHT_DECAY = 0.0005
LEARNING_RATE = 5e-3
LEARNING_RATE_D = 1e-4
NUM_STEPS = 15000
NUM_STEPS_STOP = 10000  # Use damping instead of early stopping
ITER_SIZE=1
PREHEAT_STEPS = 0 #int(NUM_STEPS / 20)
POWER = 0.9
LAMBDA_SEG = 0.1
LAMBDA_ADV_TARGET1 = 0.0002
LAMBDA_ADV_TARGET2 = 0.001


TARGET_SET = TARGET_SET

EVAL_EVERY=2000
TARGET_SET = TARGET_SET
SOURCE_DATA_CONFIG=SOURCE_DATA_CONFIG
TARGET_DATA_CONFIG=TARGET_DATA_CONFIG
EVAL_DATA_CONFIG=EVAL_DATA_CONFIG