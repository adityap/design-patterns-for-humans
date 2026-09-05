public interface IDoor
{
    float GetWidth();
    float GetHeight();
}

public class WoodenDoor : IDoor
{
    private readonly float width;
    private readonly float height;

    public WoodenDoor(float width, float height)
    {
        this.width = width;
        this.height = height;
    }

    public float GetWidth() => width;
    public float GetHeight() => height;
}

public static class DoorFactory
{
    public static IDoor MakeDoor(float width, float height)
    {
        return new WoodenDoor(width, height);
    }
}

public static class Program
{
    public static void Main()
    {
        var door = DoorFactory.MakeDoor(100, 200);
        Console.WriteLine($"Width: {door.GetWidth()}");
        Console.WriteLine($"Height: {door.GetHeight()}");
    }
}
