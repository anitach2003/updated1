# DATA
dataset = 'raildb'
data_root = '/content/updated1/Rail-DB/'

# TRAIN
epoch = 100
batch_size = 32
optimizer = 'Adam'    #['SGD','Adam']
# learning_rate = 0.1
learning_rate = 1e-4
weight_decay = 1e-5
momentum = 0.9

scheduler = 'cos'     #['multi', 'cos']
# steps = [50,75]
gamma  = 0.1
warmup = 'linear'
warmup_iters = 100

# NETWORK
backbone = '18'
griding_num = 200
cls_num_per_lane = 52

# EXP
note = 'test'

log_path = '/content/updated1/Rail-DB/log'

# FINETUNE or RESUME MODEL PATH
finetune = None
resume = None

# TEST
test_model = '/content/updated1/Rail-DB/log/test_model.pth'
test_work_dir = '/content/updated1/Rail-DB/test/'

num_lanes = 4
type = 'all'
