var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var shape = /** @class */ (function () {
    function shape() {
    }
    return shape;
}());
var triangle = /** @class */ (function (_super) {
    __extends(triangle, _super);
    function triangle(a, b, c, height) {
        var _this = _super.call(this) || this;
        _this.side_A = a;
        _this.side_B = b;
        _this.side_C = c;
        _this.height = height;
        return _this;
    }
    triangle.prototype.get_area = function () {
        return (this.side_A * this.height) / 2;
    };
    triangle.prototype.get_perimeter = function () {
        return (this.side_A + this.side_B + this.side_C);
    };
    return triangle;
}(shape));
var square = /** @class */ (function (_super) {
    __extends(square, _super);
    function square(side) {
        var _this = _super.call(this) || this;
        _this.side = side;
        return _this;
    }
    square.prototype.get_area = function () {
        return this.side * this.side;
    };
    square.prototype.get_perimeter = function () {
        return this.side * 4;
    };
    return square;
}(shape));
var circle = /** @class */ (function (_super) {
    __extends(circle, _super);
    function circle(radius) {
        var _this = _super.call(this) || this;
        _this.radius = radius;
        return _this;
    }
    circle.prototype.get_area = function () {
        return Math.PI * this.radius * this.radius;
    };
    circle.prototype.get_perimeter = function () {
        return 2 * Math.PI * this.radius;
    };
    circle.prototype.get_radius = function () {
        return this.radius;
    };
    return circle;
}(shape));
var tri = new triangle(2, 4, 5, 2);
var sqr = new square(4);
var crc = new circle(3);
var shapes = [tri, sqr, crc];
for (var _i = 0, shapes_1 = shapes; _i < shapes_1.length; _i++) {
    var _shape = shapes_1[_i];
    console.log("Area:", _shape.get_area());
    console.log("Perimeter:", _shape.get_perimeter());
    if (_shape instanceof circle) {
        console.log("Raio:", _shape.get_radius());
    }
}
