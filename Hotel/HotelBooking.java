import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HotelBooking extends Remote {
    // Book a room for a specific guest
    String bookRoom(String guestName, int roomNumber) throws RemoteException;
    
    // Cancel a booking for a specific guest
    String cancelBooking(String guestName) throws RemoteException;
    
    // Get current bookings (for demonstration)
    String listBookings() throws RemoteException;
}







/* Terminal 1:
javac *.java

start rmiregistry

java HotelBookingServer

Terminal 2:
java HotelBookingClient 
*/