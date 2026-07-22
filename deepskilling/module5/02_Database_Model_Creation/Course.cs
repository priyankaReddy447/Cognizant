using Microsoft.EntityFrameworkCore;
using EFCore8StudentManagement.Models;
namespace EFCore8StudentManagement.Data;
public class ApplicationDbContext:DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options):base(options){}
    public DbSet<Student> Students=>Set<Student>();
    public DbSet<Course> Courses=>Set<Course>();
    public DbSet<Enrollment> Enrollments=>Set<Enrollment>();
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Enrollment>()
            .HasOne(e=>e.Student).WithMany(s=>s.Enrollments).HasForeignKey(e=>e.StudentId);
        modelBuilder.Entity<Enrollment>()
            .HasOne(e=>e.Course).WithMany(c=>c.Enrollments).HasForeignKey(e=>e.CourseId);
    }
}
