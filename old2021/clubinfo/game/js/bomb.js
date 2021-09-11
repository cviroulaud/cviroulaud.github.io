class Bomb extends Phaser.GameObjects.Sprite {
constructor(config) {
  super(
        config.scene,
        config.x,
        config.y,
        config.key,
        config.frame
        );
  config.scene.add.existing(this);
  config.scene.physics.add.existing(this);
  }
};
