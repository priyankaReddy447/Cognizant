using Moq; class Demo{static void Main(){var m=new Mock<ICalculator>();m.Setup(x=>x.Add(1,2)).Returns(3);System.Console.WriteLine(m.Object.Add(1,2));}}
