// source: devices.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

goog.provide('proto.devices.Chimera');

goog.require('jspb.BinaryReader');
goog.require('jspb.BinaryWriter');
goog.require('jspb.Message');
goog.require('proto.devices.Bms');
goog.require('proto.devices.Ecu');
goog.require('proto.devices.Encoder');
goog.require('proto.devices.Imu');
goog.require('proto.devices.Inverter');
goog.require('proto.devices.Pedals');
goog.require('proto.devices.Steer');

/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.devices.Chimera = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.devices.Chimera.repeatedFields_, null);
};
goog.inherits(proto.devices.Chimera, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.devices.Chimera.displayName = 'proto.devices.Chimera';
}

/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.devices.Chimera.repeatedFields_ = [1,2,3,4,5,6,7,8,9,10,11];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.devices.Chimera.prototype.toObject = function(opt_includeInstance) {
  return proto.devices.Chimera.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.devices.Chimera} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.devices.Chimera.toObject = function(includeInstance, msg) {
  var f, obj = {
    accelList: jspb.Message.toObjectList(msg.getAccelList(),
    proto.devices.Imu.toObject, includeInstance),
    gyroList: jspb.Message.toObjectList(msg.getGyroList(),
    proto.devices.Imu.toObject, includeInstance),
    encoderLeftList: jspb.Message.toObjectList(msg.getEncoderLeftList(),
    proto.devices.Encoder.toObject, includeInstance),
    encoderRightList: jspb.Message.toObjectList(msg.getEncoderRightList(),
    proto.devices.Encoder.toObject, includeInstance),
    bmsLvList: jspb.Message.toObjectList(msg.getBmsLvList(),
    proto.devices.Bms.toObject, includeInstance),
    bmsHvList: jspb.Message.toObjectList(msg.getBmsHvList(),
    proto.devices.Bms.toObject, includeInstance),
    inverterLeftList: jspb.Message.toObjectList(msg.getInverterLeftList(),
    proto.devices.Inverter.toObject, includeInstance),
    inverterRightList: jspb.Message.toObjectList(msg.getInverterRightList(),
    proto.devices.Inverter.toObject, includeInstance),
    pedalList: jspb.Message.toObjectList(msg.getPedalList(),
    proto.devices.Pedals.toObject, includeInstance),
    steerList: jspb.Message.toObjectList(msg.getSteerList(),
    proto.devices.Steer.toObject, includeInstance),
    ecuList: jspb.Message.toObjectList(msg.getEcuList(),
    proto.devices.Ecu.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.devices.Chimera}
 */
proto.devices.Chimera.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.devices.Chimera;
  return proto.devices.Chimera.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.devices.Chimera} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.devices.Chimera}
 */
proto.devices.Chimera.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.devices.Imu;
      reader.readMessage(value,proto.devices.Imu.deserializeBinaryFromReader);
      msg.addAccel(value);
      break;
    case 2:
      var value = new proto.devices.Imu;
      reader.readMessage(value,proto.devices.Imu.deserializeBinaryFromReader);
      msg.addGyro(value);
      break;
    case 3:
      var value = new proto.devices.Encoder;
      reader.readMessage(value,proto.devices.Encoder.deserializeBinaryFromReader);
      msg.addEncoderLeft(value);
      break;
    case 4:
      var value = new proto.devices.Encoder;
      reader.readMessage(value,proto.devices.Encoder.deserializeBinaryFromReader);
      msg.addEncoderRight(value);
      break;
    case 5:
      var value = new proto.devices.Bms;
      reader.readMessage(value,proto.devices.Bms.deserializeBinaryFromReader);
      msg.addBmsLv(value);
      break;
    case 6:
      var value = new proto.devices.Bms;
      reader.readMessage(value,proto.devices.Bms.deserializeBinaryFromReader);
      msg.addBmsHv(value);
      break;
    case 7:
      var value = new proto.devices.Inverter;
      reader.readMessage(value,proto.devices.Inverter.deserializeBinaryFromReader);
      msg.addInverterLeft(value);
      break;
    case 8:
      var value = new proto.devices.Inverter;
      reader.readMessage(value,proto.devices.Inverter.deserializeBinaryFromReader);
      msg.addInverterRight(value);
      break;
    case 9:
      var value = new proto.devices.Pedals;
      reader.readMessage(value,proto.devices.Pedals.deserializeBinaryFromReader);
      msg.addPedal(value);
      break;
    case 10:
      var value = new proto.devices.Steer;
      reader.readMessage(value,proto.devices.Steer.deserializeBinaryFromReader);
      msg.addSteer(value);
      break;
    case 11:
      var value = new proto.devices.Ecu;
      reader.readMessage(value,proto.devices.Ecu.deserializeBinaryFromReader);
      msg.addEcu(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.devices.Chimera.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.devices.Chimera.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.devices.Chimera} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.devices.Chimera.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getAccelList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.devices.Imu.serializeBinaryToWriter
    );
  }
  f = message.getGyroList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      2,
      f,
      proto.devices.Imu.serializeBinaryToWriter
    );
  }
  f = message.getEncoderLeftList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      3,
      f,
      proto.devices.Encoder.serializeBinaryToWriter
    );
  }
  f = message.getEncoderRightList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      4,
      f,
      proto.devices.Encoder.serializeBinaryToWriter
    );
  }
  f = message.getBmsLvList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      5,
      f,
      proto.devices.Bms.serializeBinaryToWriter
    );
  }
  f = message.getBmsHvList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      6,
      f,
      proto.devices.Bms.serializeBinaryToWriter
    );
  }
  f = message.getInverterLeftList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      7,
      f,
      proto.devices.Inverter.serializeBinaryToWriter
    );
  }
  f = message.getInverterRightList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      8,
      f,
      proto.devices.Inverter.serializeBinaryToWriter
    );
  }
  f = message.getPedalList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      9,
      f,
      proto.devices.Pedals.serializeBinaryToWriter
    );
  }
  f = message.getSteerList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      10,
      f,
      proto.devices.Steer.serializeBinaryToWriter
    );
  }
  f = message.getEcuList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      11,
      f,
      proto.devices.Ecu.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Imu accel = 1;
 * @return {!Array<!proto.devices.Imu>}
 */
proto.devices.Chimera.prototype.getAccelList = function() {
  return /** @type{!Array<!proto.devices.Imu>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.devices.Imu, 1));
};


/**
 * @param {!Array<!proto.devices.Imu>} value
 * @return {!proto.devices.Chimera} returns this
*/
proto.devices.Chimera.prototype.setAccelList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.devices.Imu=} opt_value
 * @param {number=} opt_index
 * @return {!proto.devices.Imu}
 */
proto.devices.Chimera.prototype.addAccel = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.devices.Imu, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.devices.Chimera} returns this
 */
proto.devices.Chimera.prototype.clearAccelList = function() {
  return this.setAccelList([]);
};


/**
 * repeated Imu gyro = 2;
 * @return {!Array<!proto.devices.Imu>}
 */
proto.devices.Chimera.prototype.getGyroList = function() {
  return /** @type{!Array<!proto.devices.Imu>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.devices.Imu, 2));
};


/**
 * @param {!Array<!proto.devices.Imu>} value
 * @return {!proto.devices.Chimera} returns this
*/
proto.devices.Chimera.prototype.setGyroList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 2, value);
};


/**
 * @param {!proto.devices.Imu=} opt_value
 * @param {number=} opt_index
 * @return {!proto.devices.Imu}
 */
proto.devices.Chimera.prototype.addGyro = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 2, opt_value, proto.devices.Imu, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.devices.Chimera} returns this
 */
proto.devices.Chimera.prototype.clearGyroList = function() {
  return this.setGyroList([]);
};


/**
 * repeated Encoder encoder_left = 3;
 * @return {!Array<!proto.devices.Encoder>}
 */
proto.devices.Chimera.prototype.getEncoderLeftList = function() {
  return /** @type{!Array<!proto.devices.Encoder>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.devices.Encoder, 3));
};


/**
 * @param {!Array<!proto.devices.Encoder>} value
 * @return {!proto.devices.Chimera} returns this
*/
proto.devices.Chimera.prototype.setEncoderLeftList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 3, value);
};


/**
 * @param {!proto.devices.Encoder=} opt_value
 * @param {number=} opt_index
 * @return {!proto.devices.Encoder}
 */
proto.devices.Chimera.prototype.addEncoderLeft = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 3, opt_value, proto.devices.Encoder, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.devices.Chimera} returns this
 */
proto.devices.Chimera.prototype.clearEncoderLeftList = function() {
  return this.setEncoderLeftList([]);
};


/**
 * repeated Encoder encoder_right = 4;
 * @return {!Array<!proto.devices.Encoder>}
 */
proto.devices.Chimera.prototype.getEncoderRightList = function() {
  return /** @type{!Array<!proto.devices.Encoder>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.devices.Encoder, 4));
};


/**
 * @param {!Array<!proto.devices.Encoder>} value
 * @return {!proto.devices.Chimera} returns this
*/
proto.devices.Chimera.prototype.setEncoderRightList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 4, value);
};


/**
 * @param {!proto.devices.Encoder=} opt_value
 * @param {number=} opt_index
 * @return {!proto.devices.Encoder}
 */
proto.devices.Chimera.prototype.addEncoderRight = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 4, opt_value, proto.devices.Encoder, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.devices.Chimera} returns this
 */
proto.devices.Chimera.prototype.clearEncoderRightList = function() {
  return this.setEncoderRightList([]);
};


/**
 * repeated Bms bms_lv = 5;
 * @return {!Array<!proto.devices.Bms>}
 */
proto.devices.Chimera.prototype.getBmsLvList = function() {
  return /** @type{!Array<!proto.devices.Bms>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.devices.Bms, 5));
};


/**
 * @param {!Array<!proto.devices.Bms>} value
 * @return {!proto.devices.Chimera} returns this
*/
proto.devices.Chimera.prototype.setBmsLvList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 5, value);
};


/**
 * @param {!proto.devices.Bms=} opt_value
 * @param {number=} opt_index
 * @return {!proto.devices.Bms}
 */
proto.devices.Chimera.prototype.addBmsLv = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 5, opt_value, proto.devices.Bms, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.devices.Chimera} returns this
 */
proto.devices.Chimera.prototype.clearBmsLvList = function() {
  return this.setBmsLvList([]);
};


/**
 * repeated Bms bms_hv = 6;
 * @return {!Array<!proto.devices.Bms>}
 */
proto.devices.Chimera.prototype.getBmsHvList = function() {
  return /** @type{!Array<!proto.devices.Bms>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.devices.Bms, 6));
};


/**
 * @param {!Array<!proto.devices.Bms>} value
 * @return {!proto.devices.Chimera} returns this
*/
proto.devices.Chimera.prototype.setBmsHvList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 6, value);
};


/**
 * @param {!proto.devices.Bms=} opt_value
 * @param {number=} opt_index
 * @return {!proto.devices.Bms}
 */
proto.devices.Chimera.prototype.addBmsHv = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 6, opt_value, proto.devices.Bms, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.devices.Chimera} returns this
 */
proto.devices.Chimera.prototype.clearBmsHvList = function() {
  return this.setBmsHvList([]);
};


/**
 * repeated Inverter inverter_left = 7;
 * @return {!Array<!proto.devices.Inverter>}
 */
proto.devices.Chimera.prototype.getInverterLeftList = function() {
  return /** @type{!Array<!proto.devices.Inverter>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.devices.Inverter, 7));
};


/**
 * @param {!Array<!proto.devices.Inverter>} value
 * @return {!proto.devices.Chimera} returns this
*/
proto.devices.Chimera.prototype.setInverterLeftList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 7, value);
};


/**
 * @param {!proto.devices.Inverter=} opt_value
 * @param {number=} opt_index
 * @return {!proto.devices.Inverter}
 */
proto.devices.Chimera.prototype.addInverterLeft = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 7, opt_value, proto.devices.Inverter, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.devices.Chimera} returns this
 */
proto.devices.Chimera.prototype.clearInverterLeftList = function() {
  return this.setInverterLeftList([]);
};


/**
 * repeated Inverter inverter_right = 8;
 * @return {!Array<!proto.devices.Inverter>}
 */
proto.devices.Chimera.prototype.getInverterRightList = function() {
  return /** @type{!Array<!proto.devices.Inverter>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.devices.Inverter, 8));
};


/**
 * @param {!Array<!proto.devices.Inverter>} value
 * @return {!proto.devices.Chimera} returns this
*/
proto.devices.Chimera.prototype.setInverterRightList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 8, value);
};


/**
 * @param {!proto.devices.Inverter=} opt_value
 * @param {number=} opt_index
 * @return {!proto.devices.Inverter}
 */
proto.devices.Chimera.prototype.addInverterRight = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 8, opt_value, proto.devices.Inverter, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.devices.Chimera} returns this
 */
proto.devices.Chimera.prototype.clearInverterRightList = function() {
  return this.setInverterRightList([]);
};


/**
 * repeated Pedals pedal = 9;
 * @return {!Array<!proto.devices.Pedals>}
 */
proto.devices.Chimera.prototype.getPedalList = function() {
  return /** @type{!Array<!proto.devices.Pedals>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.devices.Pedals, 9));
};


/**
 * @param {!Array<!proto.devices.Pedals>} value
 * @return {!proto.devices.Chimera} returns this
*/
proto.devices.Chimera.prototype.setPedalList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 9, value);
};


/**
 * @param {!proto.devices.Pedals=} opt_value
 * @param {number=} opt_index
 * @return {!proto.devices.Pedals}
 */
proto.devices.Chimera.prototype.addPedal = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 9, opt_value, proto.devices.Pedals, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.devices.Chimera} returns this
 */
proto.devices.Chimera.prototype.clearPedalList = function() {
  return this.setPedalList([]);
};


/**
 * repeated Steer steer = 10;
 * @return {!Array<!proto.devices.Steer>}
 */
proto.devices.Chimera.prototype.getSteerList = function() {
  return /** @type{!Array<!proto.devices.Steer>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.devices.Steer, 10));
};


/**
 * @param {!Array<!proto.devices.Steer>} value
 * @return {!proto.devices.Chimera} returns this
*/
proto.devices.Chimera.prototype.setSteerList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 10, value);
};


/**
 * @param {!proto.devices.Steer=} opt_value
 * @param {number=} opt_index
 * @return {!proto.devices.Steer}
 */
proto.devices.Chimera.prototype.addSteer = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 10, opt_value, proto.devices.Steer, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.devices.Chimera} returns this
 */
proto.devices.Chimera.prototype.clearSteerList = function() {
  return this.setSteerList([]);
};


/**
 * repeated Ecu ecu = 11;
 * @return {!Array<!proto.devices.Ecu>}
 */
proto.devices.Chimera.prototype.getEcuList = function() {
  return /** @type{!Array<!proto.devices.Ecu>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.devices.Ecu, 11));
};


/**
 * @param {!Array<!proto.devices.Ecu>} value
 * @return {!proto.devices.Chimera} returns this
*/
proto.devices.Chimera.prototype.setEcuList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 11, value);
};


/**
 * @param {!proto.devices.Ecu=} opt_value
 * @param {number=} opt_index
 * @return {!proto.devices.Ecu}
 */
proto.devices.Chimera.prototype.addEcu = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 11, opt_value, proto.devices.Ecu, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.devices.Chimera} returns this
 */
proto.devices.Chimera.prototype.clearEcuList = function() {
  return this.setEcuList([]);
};


