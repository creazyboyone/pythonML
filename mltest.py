import tensorflow as tf
tf.compat.v1.disable_eager_execution()
hello = tf.constant('Hello Tensorflow!')
sess = tf.compat.v1.Session()
print(sess.run(hello))

a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a+b))
