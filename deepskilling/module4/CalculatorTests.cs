using NUnit.Framework; public class CalculatorTests{[Test] public void AddTest(){Assert.That(new Calculator().Add(2,3),Is.EqualTo(5));}}
